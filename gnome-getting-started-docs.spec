Name:           gnome-getting-started-docs
Version:        3.14.1.0.2
Release:        3%{?dist}
Summary:        Help a new user get started in GNOME

License:        CC-BY-SA
URL:            http://help.gnome.org/
Source0:        %{name}-%{version}.tar.xz
Group:          Documentation

BuildArch:      noarch

BuildRequires:  pkgconfig
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  yelp-tools
Requires: gnome-user-docs

# https://bugzilla.redhat.com/show_bug.cgi?id=1302982
Patch0: gnome-getting-started-docs-3.14.1.0.2-EL7.3_translations.patch
Patch1: gnome-getting-started-docs-3.14.1.0.2-EL7.3_translations_for_it.patch

%description
This package contains a 'Getting Started' guide that can be viewed
with yelp. It is normally used together with gnome-initial-setup.


%package cs
Summary:        Czech translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description cs
Czech (cs) translations for the Getting Started guide videos.


%package de
Summary:        German translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description de
German (de) translations for the Getting Started guide videos.


%package es
Summary:        Spanish translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description es
Spanish (es) translations for the Getting Started guide videos.


%package fr
Summary:        French translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description fr
French (fr) translations for the Getting Started guide videos.


%package gl
Summary:        Galician translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description gl
Galician (gl) translations for the Getting Started guide videos.


%package hu
Summary:        Hungarian translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description hu
Hungarian (hu) translations for the Getting Started guide videos.


%package it
Summary:        Italian translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description it
Italian (it) translations for the Getting Started guide videos.


%package pl
Summary:        Polish translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description pl
Polish (pl) translations for the Getting Started guide videos.


%package pt_BR
Summary:        Brazilian Portuguese translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description pt_BR
Brazilian Portuguese (pt_BR) translations for the Getting Started guide videos.


%package ru
Summary:        Russian translations for gnome-getting-started-docs videos
Group:          Documentation
Requires:       gnome-getting-started-docs = %{version}-%{release}

%description ru
Russian (ru) translations for the Getting Started guide videos.


%prep
%setup -q
%patch0 -p1 -b gnome-getting-started-docs-3.14.1.0.2-EL7.3_translations.patch
%patch1 -p1 -b gnome-getting-started-docs-3.14.1.0.2-EL7.3_translations_for_it.patch


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %{name} --all-name --with-gnome


%files -f %{name}.lang
%doc NEWS AUTHORS
%license COPYING
%exclude %{_datadir}/help/cs/gnome-help/figures/
%exclude %{_datadir}/help/de/gnome-help/figures/
%exclude %{_datadir}/help/es/gnome-help/figures/
%exclude %{_datadir}/help/fr/gnome-help/figures/
%exclude %{_datadir}/help/gl/gnome-help/figures/
%exclude %{_datadir}/help/hu/gnome-help/figures/
%exclude %{_datadir}/help/it/gnome-help/figures/
%exclude %{_datadir}/help/pl/gnome-help/figures/
%exclude %{_datadir}/help/pt_BR/gnome-help/figures/
%exclude %{_datadir}/help/ru/gnome-help/figures/

%files cs
%{_datadir}/help/cs/gnome-help/figures/

%files de
%{_datadir}/help/de/gnome-help/figures/

%files es
%{_datadir}/help/es/gnome-help/figures/

%files fr
%{_datadir}/help/fr/gnome-help/figures/

%files gl
%{_datadir}/help/gl/gnome-help/figures/

%files hu
%{_datadir}/help/hu/gnome-help/figures/

%files it
%{_datadir}/help/it/gnome-help/figures/

%files pl
%{_datadir}/help/pl/gnome-help/figures/

%files pt_BR
%{_datadir}/help/pt_BR/gnome-help/figures/

%files ru
%{_datadir}/help/ru/gnome-help/figures/


%changelog
* Thu Jun 23 2016 Petr Kovar <pkovar@redhat.com> - 3.14.1.0.2-3
- Update it translation
- Resolves: rhbz#1302982

* Wed Mar 30 2016 Petr Kovar <pkovar@redhat.com> - 3.14.1.0.2-2
- Update translations
- Resolves: rhbz#1302982

* Wed Jul 15 2015 Petr Kovar <pkovar@redhat.com> - 3.14.1.0.2-1
- Update to 3.14.1.0.2
- Resolves: rhbz#1184036

* Wed Jul 01 2015 Petr Kovar <pkovar@redhat.com> - 3.14.1.0.1-1
- Update to 3.14.1.0.1
- Resolves: rhbz#1174430

* Wed Jun 10 2015 Matthias Clasen <mclasen@redhat.com> - 3.14.1-1
- Update to 3.14.1
- Add subpackages for fr and ru video translations
Resolves: #1174430

* Wed Jan 22 2014 Petr Kovar <pkovar@redhat.com> - 3.8.3.0.2-3
- Translation updates
- Resolves: rhbz#1030341

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.3.0.2-2
- Mass rebuild 2013-12-27

* Fri Nov 08 2013 Petr Kovar <pkovar@redhat.com> - 3.8.3.0.2-1
- Update to 3.8.3.0.2
- Drop the intro video
- Resolves: rhbz#982731

* Wed Jul 31 2013 Petr Kovar <pkovar@redhat.com> - 3.8.3.0.1-2
- Fix Source0

* Tue Jul 30 2013 Petr Kovar <pkovar@redhat.com> - 3.8.3.0.1-1
- Update to 3.8.3.0.1
- Add symlinks for rhel-yelp-intro.webm

* Sun Jun 16 2013 Petr Kovar <pkovar@redhat.com> - 3.8.3-1
- Update to 3.8.3

* Tue May 14 2013 Petr Kovar <pkovar@redhat.com> - 3.8.2-1
- Update to 3.8.2
- Add gs-browse-web-firefox.page.patch
- Add subpackages for hu and it

* Wed Apr 17 2013 Petr Kovar <pkovar@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Petr Kovar <pkovar@redhat.com> - 3.8.0.1-1
- Update to 3.8.0.1

* Tue Mar 26 2013 Petr Kovar <pkovar@redhat.com> - 3.8.0-1
- Update to 3.8.0
- Add subpackages for translated videos

* Wed Mar 20 2013 Petr Kovar <pkovar@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Fri Mar  8 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Fri Feb 22 2013 Petr Kovar <pkovar@redhat.com> - 3.7.90-2%{?dist}
- gnome-initial-setup fix

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.2-2%{?dist}
- Add two missing files

* Tue Nov 20 2012 Matthias Clasen <mclasen@redhat.com> - 3.7.2-1%{?dist}
- Initial packaging
