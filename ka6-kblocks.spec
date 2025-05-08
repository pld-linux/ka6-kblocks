#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kblocks
Summary:	Kblocks
Name:		ka6-%{kaname}
Version:	25.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7bb0cfefa4ea93734281aa6a6f5e8bc8
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Qml-devel >= 5.11.1
BuildRequires:	Qt6Quick-devel >= 5.11.1
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBlocks is the classic falling blocks game. The idea is to stack the
falling blocks to create horizontal lines without any gaps. When a
line is completed it is removed, and more space is available in the
play area. When there is not enough space for blocks to fall, the game
is over.

%description -l pl.UTF-8
KBlocks jest klasyczną grą w spadające bloki. Ideą gry jest układać
spadające bloki tak, aby tworzyły poziome linie bez przerw. Kompletne
linie są usuwane i robi się więcej miejsca w obszarze gry. Gdy nie ma
już miejsca na spadające bloki, gra się kończy.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblocks
%{_desktopdir}/org.kde.kblocks.desktop
%{_datadir}/config.kcfg/kblocks.kcfg
%{_iconsdir}/hicolor/128x128/apps/kblocks.png
%{_iconsdir}/hicolor/16x16/apps/kblocks.png
%{_iconsdir}/hicolor/22x22/apps/kblocks.png
%{_iconsdir}/hicolor/32x32/apps/kblocks.png
%{_iconsdir}/hicolor/48x48/apps/kblocks.png
%{_iconsdir}/hicolor/64x64/apps/kblocks.png
%{_datadir}/kblocks
%{_datadir}/metainfo/org.kde.kblocks.appdata.xml
%{_datadir}/qlogging-categories6/kblocks.categories
%{_datadir}/knsrcfiles/kblocks.knsrc
%{_datadir}/qlogging-categories6/kblocks.renamecategories
