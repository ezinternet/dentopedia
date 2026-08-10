---
name: clinical-quiz-gate
description: After writing a wiki overview page, generate 3 clinical case questions and verify the synthesis is clinically sound before committing. Use for wiki/overviews/ pages only.
argument-hint: [overview-stem]
model: opus
allowed-tools: Read, Bash
---

# Clinical Quiz Gate

Verify that a newly written `wiki/overviews/` page is clinically coherent before it enters the repo. This is the ③ gate from the impl-notes pipeline: the user must pass 2/3 questions to unlock the commit.

## Step 1 — Identify the overview

If `args` is given, read `wiki/overviews/{args}.md`.  
If no args, find the most recently modified file in `wiki/overviews/`:

```bash
ls -t wiki/overviews/*.md | head -1
```

Read the full overview.

## Step 2 — Generate 3 clinical scenarios internally

Draft **3 scenario questions + model answers** before presenting anything to the user. Each question must:

- Be grounded in a **specific claim** in the overview (name the section or paper it comes from)
- Test a **clinical decision point**, not a recall fact
  - Good: "Given a partially infected socket and ≥3mm buccal bone, what does this overview recommend for immediate implant timing?"
  - Bad: "What was the sample size of the Kan 2010 study?"
- Have a single defensible best answer derivable from the overview alone (no external knowledge needed)
- Cover **three different sections** of the overview (don't cluster)

Keep model answers internal — do not show them yet.

## Step 3 — Present questions only

Output exactly this format:

```
## Clinical Quiz — {Overview Title}

**Q1.** {scenario}

**Q2.** {scenario}

**Q3.** {scenario}

---
Answer all three below. **Passing threshold: 2/3 correct.**
2–3 correct → overview is ready, commit proceeds.
0–1 correct → review the overview first, then re-run the quiz.
```

**Hard stop here.** Do not evaluate, do not proceed, do not hint. Wait for the user's response.

## Step 4 — Evaluate after user answers

Compare each answer against your model answer:
- **PASS**: Core clinical reasoning matches the overview's recommendation. Wording can differ.
- **FAIL**: Misses the key decision point, contradicts the overview's stated evidence, or references something not in the overview.

## Step 5 — Deliver result

**If 2–3 PASS:**
```
## Quiz Result — PASS ({n}/3)

Overview is clinically sound. Ready to commit.

Run: python3 scripts/ingest-one.py --finish {stem}
```

**If 0–1 PASS:**
```
## Quiz Result — FAIL ({n}/3)

{For each FAIL: show Q number, what was expected, what was answered, and which section of the overview to revise.}

Revise those sections, then re-run: /clinical-quiz-gate {stem}
```

Do not commit on a FAIL result.

## Scope

- Only for `wiki/overviews/` pages
- Do not apply to single-paper `wiki/{category}/` pages
- Do not apply to `sources/` summaries
