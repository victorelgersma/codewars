
// sorts solution

function solution(nums){
    if (nums === null) {
        return []
    }
    return nums.sort((a,b) => a-b)
}


console.log(solution([1, 2, 10, 50, 5])); // should return [1,2,5,10,50]
console.log(solution(null)); // should return []

