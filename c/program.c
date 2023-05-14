
/*  -------------------------------------------------------------
    
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Project:        Nasqueron
    Description:    
    License:        BSD-2-Clause
    -------------------------------------------------------------    */

#include <stdio.h>
#include <stdlib.h>

/*  -------------------------------------------------------------
    
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    */

/*  -------------------------------------------------------------
    Program entry point
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    */

int main(int argc, char **argv) {
    char *foo;

    // Usage: <executable> <foo>
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <foo>\n", argv[0]);
        return 1;
    }

    foo = argv[1];

    return 0;
}
