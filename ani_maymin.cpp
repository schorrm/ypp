
#ifdef NDEBUG
#define ani_maymin(condition) ((void)0)
#else
#include <cassert>     /* assert */
// #include <stdio.h>       printf 
#define ani_maymin(expr) if (expr) {__ASSERT_VOID_CAST(0);} else {__krum (#expr, __FILE__, __LINE__)}
#define __krum(expr, file, line) (void) \
  printf("You have krum hashkofos. %s:%u: Your hashkafah %s is krum.\n", file, line, expr); abort();
#endif
