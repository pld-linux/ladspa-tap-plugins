%define		_rnam		tap-plugins
%define		docs_snap	20040817
#
Summary:	Set of LADSPA plugins for digital audio processing
Summary(pl.UTF-8):	Zestaw wtyczek LADSPA do cyfrowej obróbki dźwięku
Name:		ladspa-tap-plugins
Version:	0.7.0
Release:	2
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/tap-plugins/%{_rnam}-%{version}.tar.gz
# Source0-md5:	e3e13df63627dcf54d0a96f8125df9ee
Source1:	http://dl.sourceforge.net/tap-plugins/%{_rnam}-doc-%{docs_snap}.tar.gz
# Source1-md5:	9a320210a7a9417487ceb31d6e5c21be
Patch0:		%{name}-DESTDIR_OPTFLAGS.patch
URL:		http://tap-plugins.sourceforge.net/
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description doc
TAP plugins documentation.

%description doc -l pl.UTF-8
Dokumentacja wtyczek TAP.

%prep
%setup -qn %{_rnam}-%{version} -a1
%patch0 -p1

%build
%{__perl} -pi -e "s,\"ladspa.h\",<ladspa.h>,g" *.c
%{__make} \
	OPTFLAGS="%{rpmcflags}"

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
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*.rdf

%files doc
%defattr(644,root,root,755)
%doc %{_rnam}-doc-%{docs_snap}/*
