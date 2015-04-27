#include "gmp_factorial.h"

#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
using namespace boost::python;
 
BOOST_PYTHON_MODULE(my_booster) {
    def("factorial", fact);
}
