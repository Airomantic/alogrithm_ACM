import heapq
import io
import json
import sys
"""
[[0,30],[5,10],[15,20]]
intervals：间隔
"""

def stringToIntegerList2(input):
    return json.loads(input) #一维和二维都可以

class Solution:
    """intervals；时间间隔 """
    def minMeetingRooms(self, intervals):
        # 如果没有需要安排的会议，那么就不需要分配房间。
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # 将会议按照开始时间的递增顺序排列
        intervals.sort(key=lambda x: x[0])  # [key,value]=[start,end] ,x[0]==key==start
        # intervals是二维list，intervals[0][1]表示会议开始时间最早的结束时间
        # 添加第一次会议。我们得给第一次会议腾出一个新房间。
        heapq.heappush(free_rooms, intervals[0][1]) #此时free_rooms[0]就有intervals[0][1]=[30]
        """intervals[0][1] 放入free_rooms"""
        # For all the remaining 剩余的会议室
        for i in intervals[1:]: #free_rooms[0]总是最小的
            # i[0]表示start，i[1]表示end
            # 如果最早空出来的那个房间是空的，就把那个房间分配给这次会议
            if free_rooms[0] <= i[0]: #结束时间free_rooms[0]=intervals[0][1]跟开始时间比较
                heapq.heappop(free_rooms) #目的是逐个缩小房间空闲时间

            # 如果要分配一个新房间，我们也要添加到堆中，
            # 如果分配了一个旧的房间，那么我们也必须用'更新'的结束时间添加到堆中
            # 最小堆free_rooms list是新加入的元素如果比已加入的元素小，则从list前面加入，比它大就放在后面
            heapq.heappush(free_rooms, i[1])

        # 堆的大小告诉我们所有会议所需的最小房间
        return len(free_rooms) #最后记录的是free_rooms=[20,30]

def main():
    def readlines():
        for lines in io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8'):
            yield lines.strip('\n')
    lines=readlines()

    while True:
        try:
            line=next(lines)
            list2=stringToIntegerList2(line)
            result=Solution().minMeetingRooms(list2)
            print(result)
        except StopIteration:
            break


if __name__ == '__main__':
    main()