"""Prologicielsucces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path
from administrations import views
from administrations.views import add_etudiant,moymodiff,auditeurmodiftotal,delete_ensignant
from administrations.views import addd_etudiant,add_classe,auditeurmodif,delete_object,dashboard,dashboardcaisse,dashboardrh,savevers,saveversautre
from administrations.views import ecoleajout,anneescolairestatut,add_document, document_detail, document_download,etuclasse,etuclassetemplate
from django.contrib.auth import views as auth_views
from accounts.views import login_user
from accounts.views import logout_user,signup_page
from auditeurs.views import etudiantespace
from auditeurs.views import enseignantespace,etuclasseauditeur,soumettre_message,soumettre_messageens
from auditeurs.views import espaceliste,add_documentp
from django.conf import settings
from django.conf.urls.static import static
from administrations.views import generer_rapport
from accounts.views import inscription_utilisateur, modifier_utilisateur, supprimer_utilisateur



urlpatterns = [
    path("admin/", admin.site.urls),

    path('dashboard', views.menusuper, name='dashboard'),
    path('academique/dashboard', views.dashboardacad, name='dashboardacademique'),
    path('caisse/dashboard', views.dashboardcaisse, name='dashboardcaisse'),
    path('ressourceshumaines/dashboard', views.dashboardrh, name='dashboardrh'),
    path('administration/menu', views.menu, name='menu'),
    path('administrationsuper/user/liste', views.user, name='user'),
    path('academique/dashboardmenu', views.dashboard, name='dashboardmenu'),
    path('administrationsuper/user/', inscription_utilisateur, name='ajoutuser'),
    path('administrationsuper/user/<int:utilisateur_id>/modifier/', modifier_utilisateur, name='modifieruser'),
    path('administrationsuper/user/<int:utilisateur_id>/supprimer/', supprimer_utilisateur, name='supprimeruser'),
    
    path('rapport/', generer_rapport, name='generer_rapport'),
    # Autres URLs de votre application...

    path('ressourceshumaines/personnel', views.personnelliste, name='listepersonnelrh'),
    path('ressourceshumaines/contact', views.personnellistecont, name='listecontact'),
    path('ressourceshumaines/personnel/autorisation/<int:id>/<int:iid>/<int:iiid>', views.ajoutautopers, name='autopers'),
    path('ressourceshumaines/personnel/autorisation/<int:id>/modification', views.autopersmodif, name='autopersmodif'),
    path('ressourceshumaines/personnel/autorisation/<int:id>/supprimer/', views.autopersdelete, name='autopersdelete'),
    path('ressourceshumaines/personnel/autorisations', views.personnelauto, name='listepersonnelauto'),

    path('ressourceshumaines/personnel/enseignant', views.enseignantlistepers, name='enseignantlistepers'),
    path('ressourceshumaines/personnel/enseignant/autorisation/<int:id>/<int:iid>/>', views.ajoutautoens, name='autoens'),
    path('ressourceshumaines/personnel/enseignant/autorisation/<int:id>/modification', views.autoensmodif, name='autoensmodif'),
    path('ressourceshumaines/personnel/enseignant/autorisation/<int:id>/supprimer/', views.autoensdelete, name='autoensdelete'),
    path('ressourceshumaines/personnel/enseignant/autorisations', views.ensauto, name='listeensauto'),

    path('ressourceshumaines/personnel/auditeurs', views.eturh, name='listeauditeurrh'),
    path('ressourceshumaines/personnel/auditeur/autorisation/<int:id>/<int:iid>/>', views.ajoutautoaud, name='autoaud'),
    path('ressourceshumaines/personnel/auditeur/autorisation/<int:id>/modification', views.autoaudmodif, name='autoaudmodif'),
    path('ressourceshumaines/personnel/auditeur/autorisation/<int:id>/supprimer/', views.autoauddelete, name='autoauddelete'),
    path('ressourceshumaines/personnel/auditeur/autorisations', views.audauto, name='listeaudauto'),

    path('ressourceshumaines/personnel/mission/<int:id>/<int:iid>/<int:iiid>', views.misajout, name='mispers'),
    path('ressourceshumaines/personnel/mission/<int:id>/modification', views.mismodif, name='mismodif'),
    path('ressourceshumaines/personnel/mission/<int:id>/supprimer/', views.misdelete, name='misdelete'),
    path('ressourceshumaines/personnel/mission', views.mispersonnel, name='listemis'),
    path('ressourceshumaines/auditeur/user/liste', views.auditeuruserrh, name='auditeuruserrh'),
    path('ressourceshumaines/enseignant/user/liste', views.enseignantuserrh, name='enseignantuserrh'),
    path('ressourceshumaines/personnel/ajout', views.personnelajout, name='personnelbase'),


    path('', views.etu, name='liste'),
    path('caisse/dashboard/inscription', views.etunon, name='listenon'),
    path('caisse/dashboard/liste/inscription', views.listeinscrit, name='listeinscrit'),
    path('caisse/dashboard/historique/paiement/journalier', views.listepaiejour, name='listepaiejour'),
    path('caisse/dashboard/historique/paiement/anneescolaire', views.listepaieannee, name='listepaieannee'),
    path('etudiantadd', addd_etudiant, name='etuadd'),
    path('etudiantaddclasse/<int:ecole>/<int:clas>/<int:niv>/', views.addd_etudiantclasse, name='etuaddclasse'),
    path('caisse/dashboard/<int:niveau_id>/<int:etudiant_id>/paiement', views.historiquevers, name='paie'),
    path('sauvegarder_historique_vers/', savevers, name='sauvegarder_historique_vers'), # type: ignore
    path('caisse/dashboard/<int:niveau_id>/<int:etudiant_id>/versement', views.historiqueversautre, name='vers'),
    path('sauvegarder_historique_paie/', saveversautre, name='sauvegarder_historique_paie'), # type: ignore

    path('academique/reinscription', views.etureins, name='listereins'),
    path('academique/reinscription/<int:id>/auditeur', views.auditeurmodifreins, name='auditeurmodifreins'),

    path('academique/liste-auditeur/<int:id>/<int:iid>/<int:iiid>', etuclasse, name='etuclasse'),
    path('academique/liste-auditeur/<int:id>/modification', auditeurmodif, name='auditeurmodif'),
    path('academique/listeauditeur/<int:id>/modification', auditeurmodiftotal, name='auditeurmodiftotal'),
    path('academique/liste-auditeur-classe/<int:id>/<int:iid>', etuclassetemplate, name='etuclassetemplate'),
    path('academique/liste-auditeur/user/liste', views.auditeuruser, name='auditeuruser'),

    path('accounts/', login_user, name='login'),
    path('accounts/log', logout_user, name='signup'),
    path('accounts/resgister', signup_page, name='register'),
    
    path('espace/auditeur', etudiantespace, name='etudiantespace'),
    path('espace/enseignant', enseignantespace, name='enseignantespace'),
    path('soumettre_message/', soumettre_message, name='soumettre_message'), # type: ignore
    path('soumettre_messageens/', soumettre_messageens, name='soumettre_messageens'), # type: ignore
    path('espace/enseignant/<int:id>/<int:iid>/document', espaceliste, name='espaceliste'), # type: ignore
    path('espace/enseignant/<int:object_id>/document/add', add_documentp, name='ajoutdoc'), # type: ignore
    path('espace/enseignant/<int:object_id>/<int:objec_id>/note', views.add_grade2, name='notebase2'), # type: ignore
    path('espace/enseignant/<int:id>/liste', views.home2, name='noteliste2'),
    path('espace/enseignant/listeauditeur/<int:id>/<int:iid>', etuclasseauditeur, name='etuclasseauditeur'),

    path('academique/institution/liste', views.ecoleliste, name='ecoleliste'),
    path('caisse/dashboard/institution/catalogue', views.ecolelistecat, name='ecolelistecat'),
    path('academique/institution/ajout', ecoleajout, name='ecolebase'),
    path('academique/institution/<int:id>/modification', views.ecolemodif, name='ecoleupdate'),
    path('academique/institution/<int:id>/classe', views.object_table, name='ecoleclasse'),
    

    path('institution/<int:id>/classeadd', add_classe, name='classeadd'),
    path('institution/<int:id>/classemodification', views.classmodif, name='classeupdate'),

    path('anneescolaire/liste', views.anneescolaireliste, name='anneescolaireliste'),
    path('anneescolaire/ajout', views.anneescolaireajout, name='anneescolairebase'),
    path('anneescolaire/<int:id>/liste', anneescolairestatut, name='anneescolairestatut'),
    path('anneescolaire/<int:id>/supprimer/', views.delete_annee, name='delete_annee'),
    path('anneescolaire/<int:id>/anneemodification', views.annemodif, name='anneemodif'),

    path('typeinstitution/liste', views.typeinstliste, name='typeinstliste'),
    path('typeinstitution/ajout', views.typeinsteajout, name='typeinstbase'),
    path('typeinstitution/<int:id>/supprimer/', views.delete_typeecole, name='deletetypeinst'),
    path('typeinstitution/<int:id>/typeinstitutionmodification', views.typeecolemodif, name='typeinstmodif'),

    path('typematiere/liste', views.typematliste, name='typematliste'),
    path('typematiere/ajout', views.typematajout, name='typematbase'),
    path('typematiere/<int:id>/supprimer/', views.delete_typemat, name='deletetypemat'),
    path('typematiere/<int:id>/typematieremodification', views.typematmodif, name='typematmodif'),

    path('matiere/liste', views.matliste, name='matliste'),
    path('matiere/ajout', views.matajout, name='matbase'),
    path('matiere/<int:id>/supprimer/', views.delete_mat, name='deletemat'),
    path('matiere/<int:id>/matieremodification', views.matmodif, name='matmodif'),

    path('session/liste', views.decoupliste, name='decoupliste'),
    path('session/ajout', views.decoupajout, name='decoupbase'),
    path('session/<int:id>/supprimer/', views.delete_decoup, name='deletedecoup'),
    path('session/<int:id>/sessionmodification', views.decoupmodif, name='decoupmodif'),

    path('caisse/catalogue/<int:id>/ajout', views.add_catalogue, name='addcatalogue'),

    path('niveauetude/liste', views.nivliste, name='nivliste'),
    path('caisse/dashboard/niveau', views.nivlistecat, name='nivlistecat'),
    path('niveauetude/ajout', views.nivajout, name='nivbase'),
    path('niveauetude/<int:id>/supprimer/', views.delete_niv, name='deleteniv'),
    path('niveauetude/<int:id>/niveaumodification', views.nivmodif, name='nivmodif'),

    path('historique/absence/liste', views.absliste, name='absliste'),
    path('historique/absence/<int:object_id>/ajout', views.absajout, name='absbase'),
    path('heureabsence/<int:id>/supprimer/', views.delete_abs, name='deleteabs'),
    path('heureabsence/<int:id>/modification', views.absmodif, name='absmodif'),

    path('Etudiant/dossierscolaire<int:id>/detail', views.dossierliste, name='dossierliste'),

    path('bulletin/<int:id>/liste', views.home, name='noteliste'),
    path('bulletin/<int:object_id>/xfr<int:objec_id>/note', views.add_grade, name='notebase'), # type: ignore
    path('bulletin/<int:id>/<int:iid>/moyenne', views.calculate_results, name='generermoyennebase'),
    path('bulletin/<int:id>/bulletin', views.homebu, name='bulletin'), # type: ignore
    path('bulletin/<int:id>/modificationmoyenne', moymodiff, name='moyupdate'), # type: ignore

    path('academique/enseignant/liste', views.enseignantliste, name='enseignantliste'),
    path('academique/enseignant/user/liste', views.enseignantuser, name='enseignantuser'),
    path('academique/enseignant/ajout', views.enseignantajout, name='enseignantbase'),
    path('academique/enseignant/<int:id>/supprimer/', delete_ensignant, name='delete_objectensignant'),
    path('academique/enseignant/<int:id>/classemodification', views.enseignantmodif, name='enseignantmodif'),

    path('academique/document/add/>', add_document, name='documentadd'),
    path('academique/document/liste', views.listedoc, name='documentlist'),
    path('academique/document/<int:document_id>/', document_detail, name='document_detail'),
    path('academique/document/<int:document_id>/download/', document_download, name='document_download'),
    path('academique/document/<int:id>/supprimer/', views.delete_doc, name='delete_doc'),
    path('academique/document/<int:id>/docmodification', views.docmodif, name='docmodif'),

    path('adminstration/avis/liste', views.avisliste, name='avisliste'),
    path('adminstration/avis/ajout', views.avisajout, name='avisbase'),
    path('adminstration/avis/<int:id>/supprimer/', views.avisdelete, name='avisdelete'),
    path('adminstration/avis/<int:id>/avismodification', views.avismodif, name='avismodif'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)