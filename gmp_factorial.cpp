#include "gmp_factorial.h"

/**
 * Computes f! using the GMP library
 *
 * Used documentation:
 * mpz_init&mpz_clear: https://gmplib.org/manual/Initializing-Integers.html
 * mpz_fac_ui: https://gmplib.org/manual/Number-Theoretic-Functions.html
 * mpz_get_str: https://gmplib.org/manual/Converting-Integers.html
 */
const char* fact(unsigned long f) {
    mpz_t x; //< A multiple precision integer
    // The functions for integer arithmetic assume that all integer objects are initialized
    mpz_init (x); //< Initialize x, and set its value to 0.
    mpz_fac_ui (x, f); //< Set 'x' to the factorial of 'f', i.e. f!
    const char *res = mpz_get_str(NULL, 10, x); //< Convert x to base 10 and store in res
    mpz_clear (x); //< Free memory
    return res;  //< Holds strlen(x)+1 bytes
}
