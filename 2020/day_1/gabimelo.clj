; input-array = (1 3 5)
(def input-array (map #(Integer/parseInt %) (clojure.string/split-lines (slurp "gabimelo.txt"))))

; summations = ([4 1 3] [8 3 5])
(def summations (for [x1 input-array
      				  x2 input-array]
  				 [(+ x1 x2) x1 x2]))

; summations-transposed = ([4 8] [1 3] [3 5])
(def summations-transposed (apply map vector summations))

(def index-for-2020 (.indexOf (nth summations-transposed 0) 2020))

(def final-answer (* (nth (nth summations index-for-2020) 1) (nth (nth summations index-for-2020) 2)))

final-answer

; pt 2

(def summations-pt2 (for [x1 input-array
      				  x2 input-array
      				  x3 input-array]
  				 [(+ x1 x2 x3) x1 x2 x3]))
(def summations-pt2-transposed (apply map vector summations))
(def index-for-2020-pt2 (.indexOf (nth summations-transposed 0) 2020))
(def final-answer-pt2 (* (nth (nth summations index-for-2020) 1) (nth (nth summations index-for-2020) 2) (nth (nth summations index-for-2020) 3)))

final-answer-pt2
