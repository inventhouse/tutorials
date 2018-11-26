# Find the longest span of each name in a Zipkin trace file

def uToS($u): $u / 1000000;  # Function to convert micros to seconds
min_by(.timestamp).timestamp as $first_ts  # Get the first timestamp

| group_by(.name)
| [
  .[]  # Unwrap the outer array of groups
  | max_by(.duration)  # Get the longest span from each group
]  # Box them into an array for sorting

| sort_by(.timestamp)  # Chronological order

| [
  .[]  # Iterate through the sorted spans
  | del(.traceId, .parentId, .id, .kind, .localEndpoint)  # Drop uninteresting fields
  | .timestamp |= (. - $first_ts)  # Update timestamp to be relative
  | (.timestamp, .duration) |= uToS(.)  # Update timestamp and duration to be in seconds
]  # Box into a final array

###
