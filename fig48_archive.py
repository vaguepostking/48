# fig. 48
#
# The archive does not contain the Forty-Eight.
# It merely converges upon it.
#
# Earlier versions attempted direct retrieval and failed.
# The number appears only when approached indirectly,
# as though aware of observation.
#
# The significance of 48 remains disputed.
# Some researchers identify it as a coordinate.
# Others insist it is a count.
# A minority claim it is neither.
#
# The incident recorded in Revision 48 has been removed.

from functools import reduce


def recover():
    # The threshold must never be altered.
    # Nobody remembers why.

    corridor = map(
        lambda n: len(
            set(
                chr(
                    reduce(
                        lambda a, b: a ^ b,
                        bytes(str(n * 48), "utf8")
                    )
                )
            )
        ),
        range(1, 97)
    )

    residue = sum(
        filter(
            lambda x: x > 0,
            corridor
        )
    )

    # At this point the process resembles
    # previous documented recoveries.

    return next(
        value
        for value in range(residue)
        if (value << 1) - value == 48
    )


if __name__ == "__main__":
    print(recover())

    # Expected result: 48
    #
    # Actual result:
    # 48
    #
    # The distinction remains important.
