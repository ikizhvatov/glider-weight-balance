# Weight balance visualisation for ASK-21 glider

Constraints for the weights (values in kg)

    f is weight in the front seat
    b is weight in the back seat

    70 <= f + 0.33b <=110 (1)
    0 <= b <= 110         (2)

There is also a max total weight constraint

    f + b <= const        (3)

where const depends on the weight of the other stuff onboard.
E.g. for NijAC gliders NF and NZ it is 194 and 220, correspondingly.
Interestingly, these limits are never reached because of (1) and (2).