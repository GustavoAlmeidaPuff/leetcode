unction mergeAlternately(word1: string, word2: string): string {
    let mergedString = ''; 
    const maxLength = Math.max(word1.length, word2.length); 

    for (let i = 0; i < maxLength; i++) {
        
        if (i < word1.length) {
            mergedString += word1[i];
        }
        
        if (i < word2.length) {
            mergedString += word2[i];
        }
    }

    return mergedString; 
};