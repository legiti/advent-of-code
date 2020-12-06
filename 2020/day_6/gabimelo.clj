(def groups (clojure.string/split (slurp "gabimelo.txt") #"\n\n"))

"Part 1:" (reduce + (map #(count (set (clojure.string/replace % #"\s" ""))) groups))

"Part 2:" (reduce + (map #(count (reduce clojure.set/intersection (map set (clojure.string/split % #"\s")))) groups))

