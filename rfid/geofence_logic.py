def is_within_allowed_hours(current_time):
    hour = current_time.tm_hour
    return 6 <= hour <= 18