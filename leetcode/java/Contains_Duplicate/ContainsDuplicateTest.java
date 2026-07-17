import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ContainsDuplicateTest {

    Solution solution = new Solution();

    @Test
    void testEmptyArray() {
        assertFalse(solution.containsDuplicate(new int[]{}));
    }

    @Test
    void testSingleElement() {
        assertFalse(solution.containsDuplicate(new int[]{5}));
    }

    @Test
    void testExample1() {
        assertTrue(solution.containsDuplicate(new int[]{1,2,3,3}));
    }

    @Test
    void testExample2() {
        assertFalse(solution.containsDuplicate(new int[]{1,2,3,4}));
    }

    @Test
    void testDuplicateAtBeginning() {
        assertTrue(solution.containsDuplicate(new int[]{1,1,2,3}));
    }

    @Test
    void testDuplicateInMiddle() {
        assertTrue(solution.containsDuplicate(new int[]{1,2,2,3}));
    }

    @Test
    void testAllDuplicates() {
        assertTrue(solution.containsDuplicate(new int[]{7,7,7,7}));
    }

    @Test
    void testNegativeNumbers() {
        assertTrue(solution.containsDuplicate(new int[]{-1,-2,-3,-1}));
    }

    @Test
    void testMixedNumbers() {
        assertTrue(solution.containsDuplicate(new int[]{-1,2,3,-1}));
    }

    @Test
    void testBoundaryValues() {
        assertFalse(solution.containsDuplicate(
                new int[]{1000000000,-1000000000}));
    }

    @Test
    void testBoundaryDuplicate() {
        assertTrue(solution.containsDuplicate(
                new int[]{1000000000,-1000000000,1000000000}));
    }
}