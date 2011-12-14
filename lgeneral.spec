%define	name	lgeneral
%define	version	1.2.2
%define	release	%mkrel 1
%define	Summary	A Panzer General clone

Name:		%{name}
Version:	%{version}
Summary:	%{Summary}
Release:	%{release}
URL:		http://lgames.sourceforge.net/index.php?project=LGeneral
Source0:	http://prdownloads.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
Source1:	http://prdownloads.sourceforge.net/lgeneral/pg-data.tar.gz
Patch0:		lgeneral-1.2.2-fix-format-errors.patch
Patch4:		lgeneral-1.2-make-lgc-pg-buildroot-aware.patch
License:	GPLv2+
Group:		Games/Strategy
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL-devel
BuildRequires:	gettext-devel
BuildRequires:	x11-server-xvfb
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer General.
You play single scenarios or whole campaigns turn by turn against a human
player or the AI. Entrenchment, rugged defense, defensive fire, surprise
contacts, surrender, unit supply, weather influence, reinforcements and other
implementations contribute to the tactical and strategic depth of the game.

%prep
%setup -q -a1
%patch0 -p1
%patch4 -p1

%build
cp /usr/share/gettext/config.rpath .
autoreconf -fi
%configure2_5x	--bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mv %{buildroot}%{_gamesdatadir}/applications %{buildroot}%{_datadir}/
%__mv %{buildroot}%{_gamesdatadir}/icons %{buildroot}%{_datadir}/

%if %{mdvver} <= 201100
%find_lang %{name} lgeneral pg
%else
%find_lang lgeneral pg %{name}.lang
%endif

# install data files
xvfb-run lgc-pg/lgc-pg -s pg-data -d %{buildroot}%{_gamesdatadir}/lgeneral

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}48.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man[16]/*
%{_gamesbindir}/*

