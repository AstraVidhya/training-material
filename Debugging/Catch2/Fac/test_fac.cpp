#define CATCH_CONFIG_MAIN
#include <catch/catch.hpp>
#include <exception>

#include "fac.h"

TEST_CASE("factorials", "[fac]") {
    REQUIRE( fac(0) == 1 );
    REQUIRE( fac(1) == 1 );
    REQUIRE( fac(5) == 120 );
    REQUIRE_THROWS_AS( fac(-1), std::invalid_argument );
}
