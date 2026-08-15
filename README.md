Phase 1: The Strategy (Day 1 Setup)

Goal: Satisfy Assignment 1 (Charter + Board).

The "Anti-black-box" rule is the most critical constraint.

1. Team Charter (Assignment 1 Deliverable)

Communication:

Channel: Slack/Discord only. No DMs for project decisions. All decisions must be in the #decisions channel.
Response Time: 2 hours during work hours. If >4 hours silent, tag @Double_6.
Conflict: If a technical disagreement lasts >15 mins, escalate to a 5-min "tie-breaker" vote. If tied, the Team Lead (rotating) decides.
 
 Work Standards:

Branch Naming: feature/<ticket-id>-<short-desc> (e.g., feature/PROJ-12-order-status).
Commit Messages: Must follow <type>: <what> - <why>.
Bad: fixed bug
Good: fix: add shipping API timeout handling - prevents 500 errors on slow carrier connections
Definition of Done (DoD): Code reviewed + Unit tests passing + Board status moved to "Done" + Commit pushed.

2. Build the Project Board (Assignment 1 Deliverable)
We need 10+ granular tasks. Do not create a task called "Build Chatbot." That violates the <4hr rule. Break it down by the MVP requirements (Order Status & Returns).

 Recommended Tech Stack for Speed:

Frontend: React (or simple HTML/JS if time is tight).
Backend: Node.js/Express.
Data: Mock JSON file (no complex DB setup needed for MVP).
Integration: Slack/Discord bot or a simple web widget.
Sample Board Tasks (Breakdown for 2 Ticket Types):

|  ID  | Task Title | Owner | Priority | Definition of Done (DoD) | Est. Hours |  
| T-01 | Setup Repo & CI Pipeline | Alice | High | Repo created, .gitignore set, "Hello World" commit passes CI. | 2 |
| T-02 | Design Data Schema (Mock JSON) | Bob | High | JSON file created with orders and returns arrays. | 1.5 | 
| T-03 | API: Get Order Status Endpoint | Alice | High | GET /api/order/:id returns JSON with status. Returns 404 if missing. | 3 | 
| T-04 | API: Get Return Policy Logic | Bob | High | GET /api/return/policy returns text based on item category. | 2 | 
| T-05 | Frontend: Chat Interface Skeleton | Charlie | Med | Input box and message history div visible. | 2.5 | 
| T-06 | Frontend: Connect Order Status API | Alice | High | User types Order ID -> UI shows status from API. | 3 | 
| T-07 | Frontend: Connect Return Logic | Bob | High | User selects "Return" -> UI shows correct policy text. | 3 | 
| T-08 | Logic: Intent Detection (Keyword) | Dave | Med | Simple regex to detect "where is" vs "return" keywords. | 2 | 
| T-09 | Testing: Unit Tests for API | Eve | High | 3 tests pass (Happy path, 404, Invalid ID). | 2 | 
| T-10 | Docs: Go-Live Readiness Note | All | Low | 1-pager drafted with "Known Broken" section. | 2 |

Action Item: Create this board in GitHub Projects, Trello, or Jira immediately. Assign owners. This is Assignment 1.

Phase 2: Execution & Audit Trail (Days 2–4)
Goal: Satisfy Assignment 2 (Collaborative Delivery) by ensuring the "Audit Log" proves equal work.

The evaluation criteria explicitly states: "Balance of Contribution (40%)" and "Process Discipline (30%)." If Imani does 80% of the commits, the team fails.

1. The Commit Convention (Critical)
Every team member must strictly follow the naming convention. This is your primary evidence.

Pattern: <type>(<scope>): <what changed> - <why it matters>
Example:
feat(api): add order status endpoint - allows frontend to fetch shipping data
fix(ui): handle empty state in chat - prevents crash when no history exists
docs: update README with setup steps - enables new devs to run locally 

2. Real-Time Board Updates
Do not wait until Friday to move cards.

Rule: When you start a task, move it to "In Progress." When you push code, move it to "Code Review." When merged, move to "Done."
Why: The audit log will compare Commit Timestamps vs. Board Movement Timestamps. If a task is "Done" on the board but the commit is 2 days later, you fail the discipline check.

3. Ensuring Contribution Balance
If you see one person dominating:

Scenario: Imani and Joseph will be doing all the backend work.
Correction: Bruce must immediately pick up the "Frontend Skeleton" (T-05) and "Unit Tests" (T-09).
Strategy: Pair program for 30 mins on a complex task, then split the commit. One person writes the code, the other writes the tests/docs, and both commit separate changes.
Commit 1 (Imani): feat: implement order logic
Commit 2 (Bruce): test: add unit tests for order logic

Checklist for Day 4 Checkpoint:

 Does every team member have at least 3 commits?

 Are all commit messages descriptive (no "fix" or "update")?

 Is the board 100% up to date with actual progress?

Are there any tasks sitting in "In Progress" for >24 hours? (If yes, escalate per Charter).
Phase 3: Delivery & Reflection (Day 5)

Goal: Satisfy Assignment 2 (Final Package) and Assignment 3 (Peer Review).

1. The Deliverable Package
You need three specific artifacts:

 1. The MVP: A working prototype (e.g., a deployed web link or a runnable script).
Must demonstrate: "Where is my order?" (Returns an answer) AND "How do I return?" (Returns a policy).
 2.The Audit Log: Export the commit history and board activity.
Tip: Run git log --oneline --all --graph and take a screenshot. Export the Trello/GitHub board activity log.
 3.The Go-Live Note:
What Works: "Order status lookup returns accurate data from mock DB."
Known Broken: "Stock availability is not implemented (out of scope for MVP)."
Handover Instructions: "To run: npm install, npm start. API docs in /docs."
