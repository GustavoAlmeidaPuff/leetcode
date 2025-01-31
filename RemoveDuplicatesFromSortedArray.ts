/*
 so... that's the solution for the problem "Remove Duplicates from Sorted Array"
 i'm not sure if this is the best solution, but it's a solution.

 basically, i firstly iterate through the array and i check if the current number is different from the number at the index position. 
 if it is, i increment the index position and i move the current number to the new position. if it's not, i increment the duplicates count.
*/

function removeDuplicates(nums: number[]): number {
    // Counter to store the number of duplicates
    let duplicatesCount = 0;
    // Index to track the position of the last unique number in the array
    let index = 0;

    
    // Iterate through the array starting from the second element
    for (let i = 1; i < nums.length; i++) {
        // If the current number is different from the number at 'index', it's unique
        if (nums[i] !== nums[index]) {
            index++; // Advance the index position
            nums[index] = nums[i]; // Move the unique number to the new position
        } else {
            duplicatesCount++; // If it's a duplicate, increment the duplicate counter
        }
    }
    
    // Fill the remaining array with "_" to indicate empty spaces
    for (let i = index + 1; i < nums.length; i++) {
        nums[i] = "_" as any;
    }
    
    // Log the count of unique numbers and the formatted array to the console
    console.log({ count: index + 1, formatedArray: nums });
    
    // Return the number of unique elements in the array
    return index + 1;
}