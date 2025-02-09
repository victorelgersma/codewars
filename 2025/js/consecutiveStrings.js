
function longestConsec(strarr, k) {
    strings = []
    n=strarr.length;
    
    if (k > n || k <= 0 || n == 0) {
        return "";
    }

    for (i=0; i<n+1-k; i++) {
        let first = strarr[i];
        for (j=0; j<k-1; j++) {
            first += strarr[i+1+j]
        }
        strings.push(first)
    }
  
    return strings.reduce((a, b) => a.length > b.length ? a : b, "");
}


