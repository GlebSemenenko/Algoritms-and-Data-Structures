package main

import "fmt"

func main() {

	sl := []int{3, 2, 4}

	fmt.Println(twoSum(sl, 6))

}

func twoSum(nums []int, target int) []int {
	// 1) скопировать массив в мэп, где ключ это индекс, а значение это значение непосредственно из массива.
	// 2) пройтись циклом по массиву и проверить, есть ли необходимое число в мэпе.

	mp := make(map[int]int) // 1
	for i, value := range nums {
		mp[i] = value
	}

	for i := range nums { // 2
		res := target - nums[i]
		fmt.Println(nums[i], res)
		for k, v := range mp { // ищу число res в значениях мапы
			if v == res && k != i {
				return []int{i, k}
			}
		}
	}
	return []int{}
	// Time Complexity: O(n²) — внешний цикл n × внутренний цикл по мапе n
	// Space Complexity: O(n) — мапа хранит все n элементов
	// Проблема: поиск значения в мапе через цикл вместо поиска по ключу O(1)
}
