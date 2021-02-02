int hammingWeight(uint32_t n) {
    int count1 = 0;
    while (n !=0){ 
    count1 ++;
    n &= n-1;}
    return count1;
    
}
