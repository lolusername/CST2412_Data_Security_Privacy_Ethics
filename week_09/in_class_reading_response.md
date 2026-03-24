# Week 9 In-Class Reading Response (Student Prompt)

## Time
8-10 minutes

## Length
150-180 words

## Official Prompt (What You Must Answer)
Write one short answer to this question:

**For the cloud workspace system from this week’s guide, should the team start with a relational model or a MongoDB-style document model, and why does the use case justify that choice?**

## Reading Excerpts

### Excerpt A: Why relational tables are often the default
When the same facts are updated from multiple places, splitting data into related tables can reduce duplication and keep one authoritative version of important fields.
This is especially helpful when accuracy, consistency, and controlled updates matter more than convenience for one read.

### Excerpt B: Why document models can be the better fit
When an application usually loads one object together, such as one workspace and its files, a document model can match the shape of the application more naturally.
This can simplify reads, especially for cloud applications that already exchange JSON.

## What Your Response Must Include

1. **Claim (1-2 sentences)**
   - Choose one model: `relational` or `document`.
   - State the use case that makes your choice reasonable.

2. **Evidence (2-3 sentences)**
   - Use at least one detail from Excerpt A and one detail from Excerpt B.
   - Explain why your chosen use case matters more here.

3. **Tradeoff (1-2 sentences)**
   - Name one realistic downside of your chosen model.
   - Explain how a team could manage that downside.

4. **Security or Privacy Connection (1-2 sentences)**
   - Explain how your model choice affects duplication, access control, or data minimization.

5. **Conclusion (1 sentence)**
   - State which model the team should start with and why.

## Sentence Starters (Optional)
- `The team should start with a ______ model because the main use case is ______.`
- `Excerpt A shows that ______, which matters here because ______.`
- `Excerpt B shows that ______, but in this situation ______ matters more.`
- `A reasonable downside is ______, and the team could reduce that risk by ______.`
- `This choice affects security/privacy because ______.`
- `Therefore, the better starting model is ______ because ______.`

## Grading Criteria
- Clear claim
- Evidence from both excerpts
- Simple use-case reasoning
- One honest tradeoff
- Clear security or privacy connection

## Common Mistakes to Avoid
- Treating one model as always best
- Listing features without connecting them to the use case
- Ignoring duplication or update risk
- Ending with vague language like `it depends` without making a decision
