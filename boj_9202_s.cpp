#include <iostream>
#include <map>
#include <string>
//Boggle
#define MAX_N   300000
#define MAX_W   8
#define MAX_L   4
using namespace std;
struct Trie {
    int sub[26];
    bool end;
    int visited;
} trie[MAX_W * MAX_N];

int tIdx = 0;
int score, maxLen, found, seq = 0;
char str[MAX_W + 1], aStr[MAX_W + 1];
int maps[MAX_L][MAX_L];
bool sels[MAX_L][MAX_L];
int mvY[8] = {0,0,1,1,1,-1,-1,-1}, mvX[8] = {1,-1,-1,0,1,-1,0,1};
int scores[MAX_W+1] = {0,0,0,1,1,2,3,5,11};

bool comp() {
    bool res = true;
    for (int i=0; i<maxLen; ++i) {
        if (aStr[i] < str[i]) break;
        else if (str[i] < aStr[i]) {
            res = false;
            break;
        }
    }
    return res;
}

void backtracking(int trieIdx, int loc, int row, int col) {
    int r, c, m;
    if (trie[trieIdx].end && trie[trieIdx].visited != seq) {
        ++found, score += scores[loc];
        trie[trieIdx].visited = seq;
        if (loc > maxLen) {
            maxLen = loc;
            for (c=0; c<loc; ++c) aStr[c] = str[c];
            aStr[loc] = '\0';
        }
        else if (loc == maxLen && !comp()) {
            for (c=0; c<loc; ++c) aStr[c] = str[c];
        }
    }

    for (m=0; m<8; ++m) {
        r = row + mvY[m], c = col + mvX[m];
        if (r < 0 || r >= MAX_L || c < 0 || c >= MAX_L || sels[r][c] || trie[trieIdx].sub[maps[r][c]] == 0) continue;
        sels[r][c] = true;
        str[loc] = maps[r][c] + 'A';
        backtracking(trie[trieIdx].sub[maps[r][c]], loc + 1, r, c);
        sels[r][c] = false;
    }
}
int main() {
    int N, i, j, t, c;
    int Q;

    trie[tIdx].end = false;
    trie[tIdx].visited = 0;
    for (j=0; j<26; ++j) trie[tIdx].sub[j] = 0;

    scanf("%d", &N);
    while (N--) {
        scanf("%s", str); //읽어들일때, 백트래킹할때 2번씀
        i = -1, c = 0;
        while (str[++i] != '\0') {
            t = str[i] - 'A';
            if (trie[c].sub[t] == 0) {
                trie[c].sub[t] = ++tIdx;
                trie[tIdx].end = false;
                trie[tIdx].visited = 0;
                for (j=0; j<26; ++j) trie[tIdx].sub[j] = 0;
            }
            c = trie[c].sub[t];
        }
        trie[c].end = true;
    }

    scanf("%d", &Q);
    while (Q--) {
        for (i=0; i<MAX_L; ++i) {
            scanf("%s", str);
            for (j=0; j<MAX_L; ++j) maps[i][j] = str[j] - 'A';
        }
        score = 0, maxLen = 0, found = 0, ++seq;
    }

    for (i=0; i<MAX_L; ++i) {
        for (j=0; j<MAX_L; ++j) {
            if (trie[0].sub[maps[i][j]] != 0) {
                sels[i][j] = true;
                str[0] = maps[i][j] + 'A';
                backtracking(trie[0].sub[maps[i][j]], 1, i, j);
                sels[i][j] = false;
            }
        }
    }

    return 0;
}
