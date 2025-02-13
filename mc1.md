# Nini Challenge 1

## Phase I
1. As an end user, I'd like to select my role when I sign up, so that my team members know what I do on the team.
2. As an end user, I'd like to select my team when I sign up, so that everyone on the platform knows which team I belng to.

## Note:
For the `Role` model, consider the following roles:
1. developer - the person on the team who works on issues
2. product owner - the person on the team who writes issues
3. scrum master - the team's coach

for the `Team` model, consider the following team names (as a suggestion):
1. Alpha - the A team
2. Bravo - the B team
3. Charlie - the C team

## Phase II
1. As a team member, I'd like to be able to view a project board containing all issues so I can understand the project's status (see below for the `Issue` model).
1.1. The project board should contain a column for each issue status.
2. As a product owner, I'd like to be able to create new issues so developers can work on them.
2.1. Only product owners can create new issues.
3. As a developer, I'd like to be able to update an issues status to represent my progress on it.
4. As a scrum master, I'd like to be able to revert an issue in the "done" column to "to do" if I do not feel the work was successfully completed.
4.1. Only scrum masters can make this change.
5. The following statuses should be available:
5.1. "to do" - "An issue for which work has not yet begun"
5.2. "in progress" - "An issue actively being worked on"
5.3. "done" - "An issue that has been completed"

## Note:
Issue model (and Status for issues):
```
from django.contrib.auth import get_user_model
from django.urls import reverse

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Issue(models.Model):
    name = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)
    description = models.TextField()
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reporter"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])

    def __str__(self):
        return self.name
```