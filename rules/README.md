# Rules Folder

This folder is for your **rule logic** – the core calculations and decision-making code that powers your solution.

## Purpose

Keep your business rules **separate** from your user interface. This separation makes your code:

- **Readable** – Others can understand the rules without digging through UI code
- **Testable** – Rules can be validated independently with unit tests
- **Explainable** – Each rule can be documented and traced back to its source

## What to Put Here

Examples of what belongs in this folder:

- Pension calculation functions
- Decision trees or rule engines
- Eligibility checks
- Tax or deduction logic
- Configuration files for rule parameters

## Best Practices

1. **Document your assumptions** – Add comments explaining why a rule works the way it does
2. **Use clear naming** – Function and variable names should reflect what the rule does
3. **Write tests** – Even simple tests help verify your logic is correct
4. **Keep rules atomic** – Small, focused functions are easier to understand and maintain

## Example Structure

```
rules/
├── README.md              # This file
├── pension_calculator.py  # Core calculation logic
├── eligibility.py         # Who qualifies for what
├── tax_rules.py           # Tax implications
└── tests/                 # Unit tests for your rules
    └── test_calculator.py
```

## Language Choice

Use whatever language your team is comfortable with. The goal is clarity, not complexity.

---

*Remember: If you can't explain how a rule works, your users won't trust the result.*
