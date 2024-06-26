"""
输入
第一行输入：数组 nums 的大小 n，取值范围 [0,10000]。

第二行输入：数组中的所有报文的序号 sn，sn 取值范围 [0,100000]。

第三行输入：需要重发的报文序号 sn，取值范围 [0,100000]。

输出
start end

说明：start 和 end 代表需要重发的报文序号 sn 在数组中的起始下标和结束下标。

样例
输入：
7
0 0 1 2 2 5 6
1

输出：
2 2

提示：
nums数组大小为7。
保存了7个报文，sn分别是0 0 1 2 2 5 6。
sn为1的报文在数组中仅有1个，下标是2，因此输出2 2。

输入：
7
0 0 1 2 2 5 6
2

输出：
3 4

提示：
nums数组大小为7。
保存了7个报文，sn分别是0 0 1 2 2 5 6。
sn为2的报文在数组中有2个，下标分别是3，4，因此输出3 4。

输入：
7
4 4 7 8 2 3 4
4

输出：
6 1

提示：
nums数组大小为7。
保存了7个报文，sn分别是4 4 7 8 2 3 4。
sn为4的报文在数组中有3个，下标分别是0，1，6，说明数组存在记录满了从头开始记录的情况，输出6 1。

输入：
7
4 4 7 8 2 3 4
6

输出：
-1 -1

提示：
nums数组大小为7。
保存了7个报文，sn分别是4 4 7 8 2 3 4。
数组中不存在sn为6的报文，因此输出-1 -1。

输入：
5
5 5 5 5 5
5

输出：
0 4

提示：
nums数组大小为5
保存了5个报文，sn分别是5 5 5 5 5
数组中所有报文sn都是5，这种情况下认为0是start，4是end，输出0 4。

"""

# 输入的nums大小
n=int(input().strip())
# 输入所有保温长度
s=list(map(int,input().strip().split()))
# 需要重发的报文
sn=int(input().strip())
def is_sorted(lst):
    before=lst[:-1]
    after=lst[1:]
    sorted_value=True
    unsorted_index=-1
    for i in range(n-1):
        if before[i]>after[i]:
            sorted_value=False
            unsorted_index=i+1
            return sorted_value,unsorted_index
    return sorted_value,unsorted_index
sorted_value,unsorted_index=is_sorted(s)
if sorted_value:
    try:
        start=s.index(sn)
    except Exception:
        start=-1
    s.reverse()
    try:
        end=n-s.index(sn)-1
    except Exception:
        end=-1
    print(start,end)
else:
    try:
        start=s[unsorted_index:].index(sn)+unsorted_index
    except Exception:
        try:
            start=s[:unsorted_index].index(sn)
        except Exception:
            start=-1
    try:
        tmp=s[:unsorted_index]
        tmp.reverse()
        end=unsorted_index-tmp.index(sn)-1
    except Exception:
        try:
            tmp=s[unsorted_index:]
            tmp.reverse()
            end=len(tmp)-tmp.index(sn)-1+unsorted_index
        except Exception:
            end=-1

    print(start,end)