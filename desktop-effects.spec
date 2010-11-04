Summary:	Switch GNOME window management and effects
Name:		desktop-effects
Version:	0.8.7
Release:	1
License:	GPL v2+
Group:		X11/Applications
URL:		http://git.fedorahosted.org/git/?p=desktop-effects.git
Source0:	https://fedorahosted.org/released/desktop-effects/%{name}-%{version}.tar.bz2
# Source0-md5:	1ae7f9ee3d231c4276af48488e47fcc8
BuildRequires:	GConf2-devel
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXcomposite-devel
Requires(pre,postun):	gtk+2
Requires:	gnome-session
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
desktop-effects provides a preference dialog to allow switching the
GNOME desktop between three different window managers: Metacity (the
standard GNOME 2 window manager), Compiz (offering 3D acceleration and
special effects), and GNOME Shell, which offers a preview of the GNOME
3 user experience.

%prep
%setup -q

%build
%configure

%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/desktop-effects.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/desktop-effects
%{_iconsdir}/hicolor/*/apps/desktop-effects.png
%{_desktopdir}/desktop-effects.desktop
%{_datadir}/desktop-effects/

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor
