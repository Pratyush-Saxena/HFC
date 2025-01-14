from django.urls import path
from HFCCore import views
from django.conf.urls import include
from django.http import HttpResponse
from django.contrib import admin
#from .feeds import LatestBlogEntries
handler404 = 'HFCCore.views.error_404'
handler500 = 'HFCCore.views.error_500'

#app_name="HFCCore"
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('problem-statements/', views.ProblemStatementsView.as_view(), name='problem_statements'),
    path('problem-statements/<title_slug>', views.ProblemDiscriptionView.as_view(), name='problem_discription'),
    #path('problem-statements/issue-area/<issue_area_slug>', views.ProblemsWithIssueareaView.as_view(), name='problem_statements_with_issuearea'),
    path('focus-areas/<issue_area_slug>/problem-statements/', views.ProblemsWithIssueareaView.as_view(), name='problem_statements_with_issuearea'),
    path('mentor/signup/', views.MentorSignup.as_view(), name='mentor_signup'),
    path('center/<hfc_center_slug>/signup/', views.CenterContributorSignup.as_view(), name='center_signup'),
    path('community/signup/', views.CommunityMemberSignup.as_view(), name='community_member_signup'),
    path('<hfc_chapter_slug>/signup/', views.ChapterContributorSignup.as_view(), name='chapter_signup'),
    path('ajax/load-expertise',views.load_area_of_expertise,name='load_area_of_expertise'),
    path('thanks/',views.thanks,name='thanks'),
    path('problem-statement/suggest/', views.ProblemStatementsSubmitView.as_view(), name='problem_statements_submit'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('community', views.CommunityView.as_view(), name='community'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('privacy-policy/',views.PrivacyPolicyView.as_view(),name = 'privacy'),
    path('terms-conditions/',views.TermsAndConditionView.as_view(),name = 'terms_conditions'),
    path('contact/',views.ContactView.as_view(),name = 'contact'),
    path('donate/',views.DonateView.as_view(),name = 'donate'),
    path('blog/',include('blog.urls')),
    path('robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file"),
    path('', include('ScreeningApp.urls')),
    path('email-users/',views.SendUserEmails.as_view(),name='email'),
    #path('latest/entries/', LatestBlogEntries(), name='blog-entry-feed'),
    path('hfcadmin/',views.admin_redirect),
    path('focus-areas/<issue_area_slug>',views.IssueAreaView.as_view(),name = 'issue_area'),
    path('focus-areas/',views.IssueAreaListView.as_view(),name = 'issue_areas'),
    path('editor/', include('django_summernote.urls')),
    path('projects/<project_slug>',views.ProjectDetailView.as_view(),name = 'project_detail'),
    path('admin/', admin.site.urls),
    path('core-team/join/',views.JobView.as_view(),name = 'job'),

    
]
