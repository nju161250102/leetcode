# LinkedList

主要的方法：

- 使用额外的头结点，不用判断当前是否为链表的开头
- 双指针（一快一慢，两个链表同时遍历）

| 序号 | 题目                                      | 思路                             |
| ---- | ----------------------------------------- | -------------------------------- |
| 2    | Add Two Numbers                           | 结点相加后移，注意最后的进位     |
| 19   | Remove Nth Node From End of List          | 双指针，间隔为n+1                |
| 21   | Merge Two Sorted Lists                    | 选择较小的结点连接，向后移动指针 |
| 24   | Swap Nodes in Pairs                       | 交换相邻结点，注意指针顺序的更改 |
| 61   | Rotate List                               | 根据余数更改链表                 |
| 82   | Remove Duplicates from Sorted List II     | 比较的是next的值，便于删除结点   |
| 83   | Remove Duplicates from Sorted List I      | 遇到相同元素删除即可             |
| 109  | Convert Sorted List to Binary Search Tree | 二分递归                         |
| 160  | Intersection of Two Linked Lists          | 两次遍历                         |
| 203  | Remove Linked List Elements               | 删除所有指定元素                 |

