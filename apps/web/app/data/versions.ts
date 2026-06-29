export const LATEST = '13.1.6'
export const LATEST_DATE = 'June 2026'

const MVN = (v: string, classifier = '') =>
  `https://repo1.maven.org/maven2/org/orekit/orekit/${v}/orekit-${v}${classifier ? `-${classifier}` : ''}.jar`

export const versions = [
  { major: 13, list: ['13.1.6', '13.1.5', '13.1.4', '13.1.3', '13.1.2', '13.1.1', '13.1', '13.0.3', '13.0.2', '13.0.1', '13.0'] },
  { major: 12, list: ['12.2.1', '12.2', '12.1.3', '12.1.2', '12.1.1', '12.1', '12.0.2', '12.0.1', '12.0'] },
  { major: 11, list: ['11.3.3', '11.3.2', '11.3.1', '11.3', '11.2.1', '11.2', '11.1.2', '11.1.1', '11.1', '11.0.2', '11.0.1', '11.0'] },
  { major: 10, list: ['10.3.2', '10.3.1', '10.3', '10.2', '10.1', '10.0'] },
  { major: 9,  list: ['9.3.1', '9.3', '9.2', '9.1', '9.0.1', '9.0'] },
  { major: 8,  list: ['8.0.1', '8.0'] },
  { major: 7,  list: ['7.2.1', '7.2', '7.1', '7.0'] },
  { major: 6,  list: ['6.1'] },
]

export const artifacts = [
  { name: `orekit-${LATEST}.jar`,         classifier: '',        size: '3.2 MB', href: MVN(LATEST) },
  { name: `orekit-${LATEST}-sources.jar`, classifier: 'sources', size: '2.1 MB', href: MVN(LATEST, 'sources') },
  { name: `orekit-${LATEST}-javadoc.jar`, classifier: 'javadoc', size: '8.4 MB', href: MVN(LATEST, 'javadoc') },
  { name: 'orekit-data.zip',              classifier: '',        size: '64 MB',  href: 'https://gitlab.orekit.org/orekit/orekit-data/-/archive/master/orekit-data-master.zip' },
]
