class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let tracker = new Map()
        for (let i = 0; i < nums.length; i++){
            const num = nums[i]
            if(tracker.has(num)){
                tracker.set(num, tracker.get(num) +1)
            }
            else{
                tracker.set(num, 1)
            }
        }

        const res = []

        for(let rnd = 0; rnd < k; rnd++){
            let bestnum = 0 
            let bestcont = 0 
            for(const [num, cont] of tracker){
                if(cont > bestcont){
                    bestcont = cont
                    bestnum = num
                }

            }
            res.push(bestnum)
            tracker.delete(bestnum)
        }

        return res
        
    }

}
