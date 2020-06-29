/* Degree array code taken from lecture 27 Rosalind Review */
/* Problem 3 on Rosalind */  

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int main() {

    FILE *infp = fopen("rosalind_deg.txt", "r");
    assert(infp != NULL);

    int n;
    int m;

    fscanf(infp, "%d %d\n", &n, &m);
    printf("n: %d, m: %d\n", n, m);

    int *degrees;

    degrees = (int *) malloc(n * sizeof(int));
    assert(degrees != NULL);

    for (int i = 0; i < n; i++){
        degrees[i] = 0;
    }

    for (int i = 0; i < m; i++){
        int u; int v;
        fscanf(infp, "%d %d\n", &u, &v);
        u--; v--;
        degrees[u]++;
        degrees[v]++;
    }

    

    /* Write output to file */
    FILE *outfp = fopen("output.txt", "w");
    for (int i = 0; i < n; i++){
        fprintf(outfp, "%d ", degrees[i]);
    }
    fprintf(outfp, "\n");
    fclose(outfp);

    free(degrees);

    return 0;
}
