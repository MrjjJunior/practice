class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        ArrayList<Integer> numbers = new ArrayList<>();
        
        for(int num: nums){
            if (numbers.contains(num)){
                return true;
            }
            numbers.add(num);
        }
        return false;
    }
}
