from django.conf.urls import patterns, include, url

urlpatterns = patterns('lrs.views',
    url(r'^$', 'home'),
    url(r'^statements/more/(?P<more_id>.{32})$', 'statements_more'),
    url(r'^statements', 'statements'),
    url(r'^activities/state', 'activity_state'),
    url(r'^activities/profile', 'activity_profile'),
    url(r'^activities', 'activities'),
    url(r'^agents/profile', 'agent_profile'),
    url(r'^agents', 'agents'),
    url(r'^actexample1/$', 'actexample1'),
    url(r'^actexample2/$', 'actexample2'),
    url(r'^about', 'about'),
    url(r'^OAuth/', include('oauth_provider.urls', namespace='oauth')),
    # just urls for some user interface and oauth2... not part of xapi

    url(r'^oauth2/user_info$', 'user_info'),
    url(r'^oauth2/', include('oauth2_provider.provider.oauth2.urls', namespace='oauth2')),

    url(r'^register', 'register'),
    url(r'^regclient2', 'reg_client2'),    
    url(r'^regclient', 'reg_client'),
    url(r'^statementvalidator', 'stmt_validator'),
    url(r'^me/statements', 'my_statements'),
    url(r'^me/download/statements', 'my_download_statements'),
    url(r'^me/activities/states', 'my_activity_states'),
    url(r'^me/activities/state', 'my_activity_state'),
    url(r'^me/apps', 'my_app_status'),
    url(r'^me/tokens2', 'delete_token2'),
    url(r'^me/tokens', 'delete_token'),
    url(r'^me/clients', 'delete_client'),
    url(r'^me', 'me')
)
