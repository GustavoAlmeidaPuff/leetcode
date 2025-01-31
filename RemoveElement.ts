/*




*/

function removeElement(nums: number[], val: number): number {
    let index = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[index] = nums[i];
            index++;
        }
    }
    return index;
}

function moveToEnd(nums: number[], val: number): number[] {
    let newLength = removeElement(nums, val);
    let count = nums.length - newLength;
    
    while (count > 0) {
        nums[newLength] = val;
        newLength++;
        count--;
    }
    
    return nums;
}