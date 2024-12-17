"""Problem #1 - Data Stream Ingestion
In a data stream, data is read in consecutive chunks - so you only have access to a certain portion of data at a given time. This is in contrast to having an entire sequence available at once. For example, Netflix and Youtube use streaming to allow users to watch chunks of video, rather than have user wait for the entire video to load - before they can start watching.

Design a system that receives a stream of strings along with timestamps. Each unique string should be printed at most every 5 seconds (i.e.,  string printed at timestamp t will prevent the same message from being printed until t + 5 seconds have passed).

All strings will be received in chronological order. Several strings may arrive at the same time.

Implement the DataStream class:
DataStream creates a data_stream object
bool should_output_data_str(int timestamp, str data_str) returns  true if the data_string should be printed in the provided timestamp, otherwise returns false

Input
data_stream = DataStream()
data_stream.should_output_data_str(timestamp=0, data_string="hello")
data_stream.should_output_data_str(timestamp=1, data_string="world")
data_stream.should_output_data_str(timestamp=6, data_string="hello")
data_stream.should_output_data_str(timestamp=7, data_string="hello")
data_stream.should_output_data_str(timestamp=8, data_string="world")

Output
[true, true, true, false, true]"""


class DataStream:

    def __init__(self):
        self.output_map = {}

    def should_output_data_str(self, timestamp, data_string):

        if data_string not in self.output_map:
            self.output_map[data_string] = 5
            return True
        else:
            if timestamp >= self.output_map[data_string]:
                self.output_map[data_string] = timestamp + 5
                return True
        return False

if __name__ == "__main__":
    data_stream = DataStream()
    print(data_stream.should_output_data_str(timestamp=0, data_string="hello"))
    print(data_stream.should_output_data_str(timestamp=1, data_string="world"))
    print(data_stream.should_output_data_str(timestamp=6, data_string="hello"))
    print(data_stream.should_output_data_str(timestamp=7, data_string="hello"))
    print(data_stream.should_output_data_str(timestamp=8, data_string="world"))

