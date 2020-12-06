(def passes (clojure.string/split-lines (slurp "gabimelo.txt")))

(defn binary-to-decimal [acc val] 
  {:position (dec (acc :position)) :value (+ (acc :value) (* (int (Math/pow 2 (dec (acc :position)))) (Character/digit val 10)))})

(defn binary-to-decimal-wrapper [binary]
  ((reduce binary-to-decimal {:position (count binary) :value 0} binary) :value))

(defn get-seat-number [pass] 
  (+ (* 8 (binary-to-decimal-wrapper (nth pass 0))) (binary-to-decimal-wrapper (nth pass 1))))

(defn get-passes-seats [passes]
  (map #(get-seat-number (split-at 7 (clojure.string/escape % {\F "0" \B "1" \L "0" \R "1"}))) passes))

(def passes-seats (get-passes-seats passes))

"Part 1:" (reduce max passes-seats)

(defn diff [coll]
  (map - coll (rest coll)))

"Part 2:"  (inc (nth (sort passes-seats) (.indexOf (diff (sort passes-seats)) -2)))
