(define (problem simple_problem)
    (:domain simple_domain)
    (:objects 
        pos1_1
        pos1_2
        pos2_1
        pos2_2)
    (:init
        (at pos1_1)
        
        (adj pos1_1 pos1_2)
        (= (distance pos1_1 pos1_2) 1)
        (adj pos1_1 pos2_1)
        (= (distance pos1_1 pos2_1) 1)
        (adj pos1_1 pos2_2)
        (= (distance pos1_1 pos2_2) 5)
        (adj pos1_2 pos2_2)
        (= (distance pos1_2 pos2_2) 1)
        (adj pos1_2 pos1_1)
        (= (distance pos1_2 pos1_1) 1)
        (adj pos1_2 pos2_1)
        (= (distance pos1_2 pos2_1) 5)
        (adj pos2_1 pos2_2)
        (= (distance pos2_1 pos2_2) 1)
        (adj pos2_1 pos1_1)
        (= (distance pos2_1 pos1_1) 1)
        (adj pos2_1 pos1_2)
        (= (distance pos2_1 pos1_2) 5)
        (adj pos2_2 pos2_1)
        (= (distance pos2_2 pos2_1) 1)
        (adj pos2_2 pos1_2)
        (= (distance pos2_2 pos1_2) 1)
        (adj pos2_2 pos1_1)
        (= (distance pos2_2 pos1_1) 5)
        (= (total-cost) 0)

    )
    (:goal (and(at pos2_2)))
    (:metric minimize(total-cost))
)