%define		pname		tap-plugins
%define		docs_ver	20140526
Summary:	Set of LADSPA plugins for digital audio processing
Summary(pl.UTF-8):	Zestaw wtyczek LADSPA do cyfrowej obróbki dźwięku
Name:		ladspa-tap-plugins
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
#Source0Download: https://github.com/tomszilagyi/tap-plugins/releases
Source0:	https://github.com/tomszilagyi/tap-plugins/archive/v%{version}/%{pname}-%{version}.tar.gz
# Source0-md5:	d36cf5f136c53f116a3f8496ad592355
Source1:	http://downloads.sourceforge.net/tap-plugins/%{pname}-doc-%{docs_ver}.tar.gz
# Source1-md5:	8af9ad9be0aac9f577056311d7ebbd5e
Patch0:		%{name}-DESTDIR_OPTFLAGS.patch
URL:		https://tomscii.sig7.se/tap-plugins/
BuildRequires:	ladspa-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of LADSPA plugins for digital audio processing, intended for use
in a professional DAW environment such as Ardour.

%description -l pl.UTF-8
Zestaw wtyczek LADSPA do cyfrowej obróbki dźwięku, których
zamierzeniem jest użycie w profesjonalnym środowisku jak np. Ardour.

%package doc
Summary:	TAP plugins documentation
Summary(pl.UTF-8):	Dokumentacja wtyczek TAP
Group:		Documentation
Suggests:	%{name} = %{version}-%{release}

%description doc
TAP plugins documentation.

%description doc -l pl.UTF-8
Dokumentacja wtyczek TAP.

%prep
%setup -qn %{pname}-%{version} -a1
%patch -P0 -p1

%{__mv} %{pname}-doc-%{docs_ver} docs

# use system ladspa header
%{__rm} ladspa.h

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README
%attr(755,root,root) %{_libdir}/ladspa/tap_autopan.so
%attr(755,root,root) %{_libdir}/ladspa/tap_chorusflanger.so
%attr(755,root,root) %{_libdir}/ladspa/tap_deesser.so
%attr(755,root,root) %{_libdir}/ladspa/tap_doubler.so
%attr(755,root,root) %{_libdir}/ladspa/tap_dynamics_m.so
%attr(755,root,root) %{_libdir}/ladspa/tap_dynamics_st.so
%attr(755,root,root) %{_libdir}/ladspa/tap_echo.so
%attr(755,root,root) %{_libdir}/ladspa/tap_eq.so
%attr(755,root,root) %{_libdir}/ladspa/tap_eqbw.so
%attr(755,root,root) %{_libdir}/ladspa/tap_limiter.so
%attr(755,root,root) %{_libdir}/ladspa/tap_pinknoise.so
%attr(755,root,root) %{_libdir}/ladspa/tap_pitch.so
%attr(755,root,root) %{_libdir}/ladspa/tap_reflector.so
%attr(755,root,root) %{_libdir}/ladspa/tap_reverb.so
%attr(755,root,root) %{_libdir}/ladspa/tap_rotspeak.so
%attr(755,root,root) %{_libdir}/ladspa/tap_sigmoid.so
%attr(755,root,root) %{_libdir}/ladspa/tap_tremolo.so
%attr(755,root,root) %{_libdir}/ladspa/tap_tubewarmth.so
%attr(755,root,root) %{_libdir}/ladspa/tap_vibrato.so
%{_datadir}/ladspa/rdf/tap-plugins.rdf
%{_datadir}/ladspa/rdf/tap_reverb.rdf

%files doc
%defattr(644,root,root,755)
%doc docs/*
