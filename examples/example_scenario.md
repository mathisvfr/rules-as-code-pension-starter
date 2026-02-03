# Example Scenario: Pension Lump-Sum Options

This document illustrates a simple scenario to help teams understand the problem space.

## The Situation

**Marie** is approaching retirement and must decide how much of her pension to take as a one-time lump sum versus a monthly annuity.

### Marie's Profile

| Attribute | Value |
|-----------|-------|
| Age | 64 |
| Total pension value | €150,000 |
| Expected retirement duration | 20 years |
| Tax bracket | 30% |

## The Options

Marie can choose to take **0%, 5%, or 10%** of her pension as a lump sum. The rest is converted to a monthly payment.

### Option A: 0% Lump Sum

- **Lump sum received:** €0
- **Monthly annuity:** ~€625/month (simplified)
- **Tax on lump sum:** €0

### Option B: 5% Lump Sum

- **Lump sum received:** €7,500
- **Monthly annuity:** ~€594/month
- **Tax on lump sum:** Varies by jurisdiction

### Option C: 10% Lump Sum

- **Lump sum received:** €15,000
- **Monthly annuity:** ~€563/month
- **Tax on lump sum:** Varies by jurisdiction

## Questions to Explore

Your solution should help users like Marie answer questions such as:

1. **Which option gives me the most total income over time?**
2. **How does each option affect my taxes?**
3. **What if I live longer or shorter than expected?**
4. **When would a lump sum make sense for me?**
5. **What are the trade-offs I should consider?**

## Beyond the Numbers

Consider how to present this information:

- Can you visualize the trade-offs?
- How do you explain uncertainty (life expectancy, inflation)?
- What assumptions are you making, and are they visible to the user?

---

*Note: These numbers are simplified for illustration. Real pension calculations involve many more factors.*
