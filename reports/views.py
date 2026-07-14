from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.db.models import Q

from .models import Issue, Reply
from .forms import IssueForm, CustomSignupForm, ReplyForm

def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_superuser:

            login(request, user)

            # Admin goes directly to Category Page
            return redirect("category_list")

        return render(
            request,
            "reports/admin_login.html",
            {
                "error": "Invalid Admin Username or Password."
            }
        )

    return render(request, "reports/admin_login.html")

@login_required
def category_list(request):
    categories = Issue.CATEGORY_CHOICES

    custom_categories = (
        Issue.objects
        .exclude(custom_category__isnull=True)
        .exclude(custom_category="")
        .values_list("custom_category", flat=True)
        .distinct()
    )

    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.submitted_by = request.user
            issue.save()
            return redirect(
                "issues_by_category",
                category=issue.get_category_display_name()
            )
    else:
        form = IssueForm()

    # ✅ define issues
    issues = Issue.objects.all().order_by("-created_at")

    return render(
        request,
        "reports/category_list.html",  # use category_list.html
        {
            "categories": categories,
            "custom_categories": custom_categories,
            "issues": issues,
            "selected_category": None,  # or remove this if not needed
            "form": form,
        }
    )

@login_required
def issues_by_category(request, category):

    categories = Issue.CATEGORY_CHOICES

    custom_categories = (
        Issue.objects
        .exclude(custom_category__isnull=True)
        .exclude(custom_category="")
        .values_list("custom_category", flat=True)
        .distinct()
    )

    # Get all issues of the selected category
    issues = Issue.objects.filter(
        Q(category=category) |
        Q(custom_category=category)
    ).order_by("-created_at")

    # Reply form
    reply_form = ReplyForm()

    # Only Superuser can reply
    if request.method == "POST" and request.user.is_superuser:

        issue_id = request.POST.get("issue_id")

        issue = get_object_or_404(
            Issue,
            id=issue_id
        )

        reply_form = ReplyForm(request.POST)

        if reply_form.is_valid():

            reply = reply_form.save(commit=False)
            reply.issue = issue
            reply.author = request.user
            reply.save()

            return redirect(
                "issues_by_category",
                category=category
            )

    return render(
        request,
        "reports/category_list.html",
        {
            "categories": categories,
            "custom_categories": custom_categories,
            "issues": issues,
            "selected_category": category,
            "reply_form": reply_form,
        }
    )

def start_page(request):
    return render(request, "reports/start.html")


def signup_view(request):

    if request.method == "POST":

        form = CustomSignupForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = CustomSignupForm()

    return render(
        request,
        "reports/signup.html",
        {
            "form": form
        }
    )



def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def issue_detail(request, issue_id):

    issue = get_object_or_404(Issue, id=issue_id)

    # Only admin can reply or update status
    if request.user.is_superuser:

        if request.method == "POST":

            # Update Status
            if "status" in request.POST:
                issue.status = request.POST.get("status")
                issue.save()

            # Add Reply
            if "message" in request.POST:
                form = ReplyForm(request.POST)

                if form.is_valid():
                    reply = form.save(commit=False)
                    reply.issue = issue
                    reply.author = request.user
                    reply.save()

            return redirect("issue_detail", issue_id=issue.id)

        form = ReplyForm()

    else:
        form = None

    return render(
        request,
        "reports/issue_detail.html",
        {
            "issue": issue,
            "form": form
        }
    )