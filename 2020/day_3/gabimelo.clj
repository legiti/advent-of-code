(def input-map (clojure.string/split-lines (slurp "gabimelo.txt")))

(defn count-tree [slope map-width status line] 
	(if 
				(and
					(= 0 (mod (status :y-coord 0) (slope :y)))
					(= \# (nth line (mod (* (status :y-coord 0) (/ (slope :x) (slope :y))) map-width)))
				)
				{:y-coord (inc (status :y-coord 0)) :trees-encountered (inc (status :trees-encountered 0))}				
				{:y-coord (inc (status :y-coord 0)) :trees-encountered (status :trees-encountered 0)}))

(defn count-trees [input-map slope]
	((reduce (partial count-tree slope (count (nth input-map 0))) {} input-map) 
			:trees-encountered))

; part 1
(count-trees input-map {:x 3 :y 1})

; part 2

(defn multiply-trees [input-map acc slope]
	(* (count-trees input-map slope) acc))

(reduce (partial multiply-trees input-map) 1 [{:x 1 :y 1} {:x 3 :y 1} {:x 5 :y 1} {:x 7 :y 1} {:x 1 :y 2}])
