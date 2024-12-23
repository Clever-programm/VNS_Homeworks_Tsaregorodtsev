import re
from datetime import datetime
from collections import defaultdict


def process_logs(logs: list[str]) -> tuple[int, list[str], list[int], list[int], list[set[str]]]:
    log_pattern = re.compile(
        r"\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] "
        r"\[(?P<player>[^\]]+)\]: (?P<event>[a-z_]+)(?: (?P<args>.+))?"
    )

    players = set()
    online_time = defaultdict(int)
    last_connected = {}
    total_blocks = 0
    player_blocks = defaultdict(int)
    achievements = defaultdict(set)

    for log in logs:
        match = log_pattern.match(log)
        if not match:
            continue

        timestamp = match.group("timestamp")
        player_name = match.group("player")
        event = match.group("event")
        args = match.group("args")

        players.add(player_name)

        if event == "connected":
            last_connected[player_name] = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        elif event == "disconnected":
            if player_name in last_connected:
                connect_time = last_connected[player_name]
                disconnect_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                online_time[player_name] += int((disconnect_time - connect_time).total_seconds())
                del last_connected[player_name]

        elif event == "block_placed":
            total_blocks += 1
            player_blocks[player_name] += 1

        elif event == "achievement_unlocked":
            achievement_name = args.strip() if args else ""
            achievements[player_name].add(achievement_name)

    for player, connect_time in last_connected.items():
        online_time[player] += int(
            (datetime.strptime(logs[-1].split("] [")[0][1:], "%Y-%m-%d %H:%M:%S") - connect_time).total_seconds())

    player_list = sorted(players)
    online_time_list = [online_time[player] for player in player_list]
    player_blocks_list = [player_blocks[player] for player in player_list]
    achievements_list = [achievements[player] for player in player_list]

    return total_blocks, player_list, online_time_list, player_blocks_list, achievements_list