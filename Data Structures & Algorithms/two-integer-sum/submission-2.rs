impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        
        use std::collections::HashMap;
        let mut new_nums:HashMap<i32,i32> = HashMap::new();

        for (index,val) in nums.iter().enumerate() {
            let remain = target-val;
            // if nums.contains(&remain){
            //     println!("something");
            // 
            new_nums.insert(remain,index as i32 );
        }
        for (index,val) in nums.iter().enumerate(){
            // if new_nums.contains_key(val){
            //    return [index,new_nums[&val]]try_into().unwrap()
            // }
            if let Some(&match_index) = new_nums.get(val) {
                if index as i32 != match_index {
                    return vec![index as i32, match_index];
                }
            }
        }
        // println!("{:?}",new_nums);
    vec![]
    }
}