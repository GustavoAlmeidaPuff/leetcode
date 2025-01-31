/*
 to start, 



*/

function removeElement(nums: number[], val: number): number {
    let index = 0; // Pointer to track the position of non-val elements
    
    for (let i = 0; i < nums.length; i++) { // Loop through the entire array
        if (nums[i] !== val) { // If the current element is not equal to val
            nums[index] = nums[i]; // Move it to the position tracked by index
            index++; // Increment the index for the next non-val element
        }
    }
    return index; // Return the new length of the array without val elements
}