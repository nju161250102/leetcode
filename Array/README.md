# Array

常用的方法是遍历，有序数组可以使用双指针夹逼遍历。

| 序号 | 题目                                   | 思路                                                         |
| ---- | -------------------------------------- | ------------------------------------------------------------ |
| 1    | Two Sum                                | 使用哈希表(map)，记录所需的另一个数和当前位置，一次遍历      |
| 15   | 3Sum                                   | 排序后遍历列表确定第一个数，使用双指针确定另外两个数，注意判断去重 |
| 16   | 3Sum Closest                           | 与上一题类似，还是使用双指针                                 |
| 26   | Remove Duplicates from Sorted Array    | 有序数组，直接遍历去重                                       |
| 27   | Remove Element                         | 将需要删除的元素通过交换位置全部移至数组末尾                 |
| 41   | First Missing Positive                 | 先排序后遍历                                                 |
| 80   | Remove Duplicates from Sorted Array II | 遍历时能够确定重复次数，最后到末尾结束后还要再判断一次       |
| 189  | Rotate Array                           | 移动数组元素                                                 |
| 299  | Bulls and Cows                         | 使用map或array记录数字出现次数                               |

