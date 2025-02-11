function plusOne(digits: number[]): number[] {
    

    let intArray = BigInt(digits.join('')) + BigInt(1);
    return intArray.toString().split('').map(Number);
    
};