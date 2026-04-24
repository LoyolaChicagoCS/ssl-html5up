# How To Contribute

## Table of Contents

- [How To Contribute](#how-to-contribute)
  - [Table of Contents](#table-of-contents)
  - [Standard Contribution Workflow](#standard-contribution-workflow)
  - [Reporting An Issue](#reporting-an-issue)
  - [Reporting A Security Vulnerability](#reporting-a-security-vulnerability)
  - [Feature Request](#feature-request)
  - [Reusing This Project](#reusing-this-project)

## Standard Contribution Workflow

Use this workflow for all non-security contributions.

1. **Open an issue**

   - Describe the bug, enhancement, or task clearly.
   - Include reproduction steps or acceptance criteria when relevant.

1. **Create a branch from `main` named `issue-<number>`**

   - Example for issue `#8`:

   ```bash
   git checkout main
   git pull origin main
   git checkout -b issue-8
   ```

1. **Resolve the issue on that branch**

   - Keep changes focused to the issue scope.
   - Run project validation checks before opening a PR.

1. **Open a PR to `main` and close the issue with a closing comment**

   - In the PR description, include a GitHub closing keyword, for example:
     - `Closes #8`
     - `Fixes #8`
     - `Resolves #8`

When the PR is merged, GitHub automatically closes the linked issue.

## Reporting An Issue

Thanks for finding an issue with our software!

Please report the bug as well as how to recreate it in our issue tracker.

## Reporting A Security Vulnerability

Thank you for reporting this to us!

Please see our [security policy](SECURITY.md) for more information.

## Feature Request

Thanks for wanting to improve our software!

Please open an issue and describe the feature in as much detail as possible.

Feature requests follow the same standard workflow above:

1. Open an issue.
1. Create `issue-<number>` from `main`.
1. Implement the feature in that branch.
1. Open a PR to `main` with a closing keyword for the issue.

## Reusing This Project

Thanks for reusing this project!

If you plan on reusing the software within an academic context, please cite us.

Else, please post your project and how it reuses this software in the discussion
forum.
