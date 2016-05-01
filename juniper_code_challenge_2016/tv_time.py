def parse_input():
    channels = int(raw_input().strip())
    commercials = [0] * channels
    for i in range(0, channels):
        adv = map(int, raw_input().strip().split(" ")[1:])
        commercials[i] = adv
    return commercials


def find_next_commercial(channel, current_time, commercials):
    ads = commercials[channel]
    for i in range(0, len(ads), 2):
        if (ads[i] <= current_time < ads[i + 1]) or current_time < ads[i]:
            return [ads[i], ads[i + 1]]
    return [None, None]


def prev_channel(current_channel, total_channels):
    if current_channel == 0:
        return total_channels - 1
    return current_channel - 1


def find_min_commerical_time(current_time, channel, commercials):
    cchannnels = len(commercials)  # number of channel. We are guaranteed to have a commercial in every channel
    if current_time >= 60:
        return 0  # your tv time is over :(
    break_start_time, break_end_time = find_next_commercial(channel, current_time, commercials)
    if break_start_time is None:
        return 0  # no more breaks in this channel from now on :)

    if current_time < break_start_time:
        # there is a break in this channel in future
        penalty_from_next_channel = find_min_commerical_time(break_start_time + 1, (channel + 1) % cchannnels,
                                                             commercials) + 1
        penalty_from_prev_channel = find_min_commerical_time(break_start_time + 1,
                                                             prev_channel(channel, cchannnels), commercials) + 1
        penalty_in_this_channel = find_min_commerical_time(break_end_time, channel, commercials) + (
            break_end_time - break_start_time)
    else:
        # currently in a break in this channel
        penalty_from_next_channel = find_min_commerical_time(current_time + 1, (channel + 1) % cchannnels,
                                                             commercials) + 1
        penalty_from_prev_channel = find_min_commerical_time(current_time + 1, prev_channel(channel, cchannnels),
                                                             commercials) + 1
        penalty_in_this_channel = find_min_commerical_time(break_end_time, channel, commercials) + (
            break_end_time - current_time)

    return min(penalty_from_next_channel, penalty_from_prev_channel, penalty_in_this_channel)


def main():
    commercials = parse_input()
    print 60 - find_min_commerical_time(0, 0, commercials)


if __name__ == '__main__':
    main()
